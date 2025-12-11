
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