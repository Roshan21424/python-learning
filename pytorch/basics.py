
'''torch is the PyTorch library'''
import torch

''' It converts Python objects (lists, numbers) into PyTorch Tensors.
A tensor = a multi-dimensional array, like:
vector → 1D tensor
matrix → 2D tensor
batch of images → 4D tensor
GPT logits → 3D tensor '''

res=torch.tensor([1,2,3,4,5],dtype=torch.long)
print(res)


'''torch.stack takes a list of tensors of the same shape and stacks them together to create a new dimension.'''
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = torch.tensor([7, 8, 9])

res=torch.stack([a, b, c])
print(res)