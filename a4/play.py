# import torch
# from torch.utils.data import Dataset, DataLoader
# from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pack_sequence, pad_packed_sequence


# class MyData(Dataset):
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         return self.data[idx]


# def collate_fn(data):
#     data.sort(key=lambda x: len(x), reverse=True)
#     data = pad_sequence(data, batch_first=True, padding_value=0)
#     return data

# # print("aaa")


# a = torch.tensor([[1, 1], [2, 1], [3, 1], [4, 1]])
# b = torch.tensor([[5, 1], [6, 1], [7, 1]])
# c = torch.tensor([[7, 1], [8, 1]])
# d = torch.tensor([[9, 1]])
# train_x = [a, b, c, d]

# data = MyData(train_x)
# # data_loader = DataLoader(
# #     data, batch_size=2, shuffle=True, collate_fn=collate_fn)
# data_loader = DataLoader(
#     data, batch_size=2, shuffle=False, collate_fn=collate_fn)
# # 采用默认的 collate_fn 会报错
# # data_loader = DataLoader(data, batch_size=2, shuffle=True)
# batch_x = iter(data_loader).next()

# print(batch_x, batch_x.shape)














# import torch

# A = torch.arange(0, 500, 1).reshape(10, 10, 5)
# B = torch.arange(0, 150, 1).reshape(10, 5, 3)
# print((A @ B)[0], (A @ B).shape)

# C = torch.arange(0, 50, 1).reshape(10, 5)
# D = torch.arange(0, 15, 1).reshape(5, 3)
# print((C @ D)[0], (C @ D).shape)

# # A = torch.randn(10, 10, 5)
# # B = torch.randn(10, 5, 3)

# # # calculate the product of the tensors
# # product_tensor = torch.matmul(A, B)

# # # print the shape of the product tensor
# # print(product_tensor.shape)
# # # (10, 10, 15)

import torch

print(torch.cuda.is_available())