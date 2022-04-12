import torch
PATH = 'pedestrian-and-vehicle-detector-adas-0001.pth'
model = torch.load(PATH)
print(model)
