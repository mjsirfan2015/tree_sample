One way to implement A tree as given would be :
```python
from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=10)

    @property
    def parent(self):
        relation = NodeRelation.objects.filter(child=self)
        if not relation.exists(): return None
        return relation.first().parent

class NodeRelation(models.Model):
    parent = models.ForeignKey(Node,on_delete=models.CASCADE,related_name='child_nodes')
    child = models.ForeignKey(Node,on_delete=models.CASCADE,related_name='parent_nodes')
```
Here a `Node` model is created to store name data and its relations to other nodes are specified by creating
a `NodeRelation` class.

#### Pros of the above code:
* Easy to understand and maintain
* Use of foreignkey to traverse the nodes.
* the parent property decorator helps to obtain the parent node easily

#### Cons of the above code:
* The above implementation is not good with large databases as it would requires large no of queries for fetching parent node
* Multiple relationships are not supported
* Does not support trees with cycles.

>In the tree that was given, D can be considered a grandchild of A

We can implement a tree count calculation using a queue

``` python
def count_node_descendants(node):
        count = 0
        queue = [node]
        while queue:
            node = queue.pop(0)
            count += len(node.child_nodes.all())
            for child in node.child_nodes.all():
                queue.append(child.child)
        return count```