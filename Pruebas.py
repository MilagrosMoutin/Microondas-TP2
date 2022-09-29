import numpy as np

eef_trans_d = 3.35669
lambda_z_transf_l1 = (3*1e8)/((1e9)*np.sqrt(eef_trans_d))
print(lambda_z_transf_l1)
l_trans_l1 = lambda_z_transf_l1 * 0.04
print(l_trans_l1)
eef_trans = 3.111
lambda_z_transf = (3*1e8)/((1e9)*np.sqrt(eef_trans))
print(lambda_z_transf)
l_trans = lambda_z_transf/4
print(l_trans)