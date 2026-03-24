# GNN Learning Pathway: UvA Tutorial 实战

## 📌 项目简介
本项目是我在学习图神经网络 (Graph Neural Networks, GNN) 过程中的实战与踩坑记录。
代码主要基于公认优质的入门教程：[UvA Deep Learning Course - Tutorial 7](https://colab.research.google.com/github/phlippe/uvadlc_notebooks/blob/master/docs/tutorial_notebooks/tutorial7/GNN_overview.ipynb)。

在此仓库中，我不仅跑通了原始代码，还添加了针对小白的详细中文注释、排雷指南以及个人学习心得。这既是我的个人 GNN 知识库，也希望能为其他初学者（或者我那位做时间序列研究的朋友 😉）提供一些参考。

## 🛠️ 环境配置指南 (Windows CPU 专属)

为了避免库版本冲突造成的“依赖地狱”，本项目强烈建议使用 Conda 隔离环境运行：

**1. 创建并激活环境**
```bash
conda create -n gnn_env python=3.9 -y
conda activate gnn_env
```

**2. 安装核心深度学习库 (CPU 版本)**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install pytorch-lightning
```

**3. 安装数据处理与可视化依赖**
```bash
pip install matplotlib seaborn tqdm ipykernel urllib3
```
> **⚠️ 避坑警告：** 如果你使用的是 VSCode 的 Jupyter Notebook，在终端安装完所有新包后，**务必在 Notebook 界面点击 Restart (重启内核)**，否则 Notebook 无法识别新安装的包，会持续报 `ModuleNotFoundError`。

## 📂 仓库结构
* `GNN_overview.ipynb`: 包含核心图构建逻辑与 GCN 代码的交互式笔记本（附带我的个人注释）。
* `README.md`: 项目说明文档。
* `.gitignore`: 避免上传过大数据集和模型的配置文件。

## 💡 学习心得与踩坑记录
1. **环境配置的黄金法则：** “终端装新包 ➡️ Notebook 重启 Kernel”。不重启，不认包。
2. **终端避坑：** 在 VSCode 中使用 Conda 环境时，应避免使用 PowerShell (PS)，最好切换至传统的 Command Prompt (CMD)，以确保 `conda activate` 成功执行。
3. **图的初印象：** 在 PyTorch 中，图并不是画出来的，而是由“节点特征矩阵 (Node Features, X)”和“边索引矩阵 (Edge Index, A)”这两个张量 (Tensor) 构成的。

## 🙏 致谢
感谢原作者 Phillip Lippe 提供的极高质量 Tutorial，以及在此过程中协助我梳理思路的 AI 助教。
