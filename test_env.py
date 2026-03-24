import torch
import pytorch_lightning as pl

# 检查 PyTorch 版本
print("PyTorch Version:", torch.__version__)

# 检查设备 (应该输出 cpu)
device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
print("当前使用的设备是:", device)