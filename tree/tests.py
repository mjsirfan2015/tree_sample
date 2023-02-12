from django.test import TestCase

from .models import Node,NodeRelation


class SampleTreeTest(TestCase):
    """
        sample tree:
        A->[B,C]
        B->[D,E]
        where the nodes in sqaure brackets are children
        inorder: D,B,E,A,C
        preorder: A,B,D,E,C
        postorder: D,E,B,C,A
    """

    def setUp(self):
        A = Node.objects.create(name="A")
        B = Node.objects.create(name="B")
        C = Node.objects.create(name="C")
        D = Node.objects.create(name="D")
        E = Node.objects.create(name="E")

        #parent B,C to A
        NodeRelation.objects.create(parent=A,child=B)
        NodeRelation.objects.create(parent=A,child=C)

        #parent D,E to B
        NodeRelation.objects.create(parent=B,child=D)
        NodeRelation.objects.create(parent=B,child=E)

    def test_parents(self):
        """
            Check if parents are set correctly
        """
        A = Node.objects.get(name="A")
        B = Node.objects.get(name="B")
        C = Node.objects.get(name="C")
        D = Node.objects.get(name="D")

        self.assertEqual(A.parent,None)
        self.assertEqual(B.parent,A)
        self.assertEqual(C.parent,A)
        self.assertEqual(D.parent,B)
