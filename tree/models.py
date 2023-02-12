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
