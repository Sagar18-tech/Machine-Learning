import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([50,100,150,200,250])

m=0
c=0
lr=0.01
epochs=1000
n=len(x)

for _ in range (epochs):
    y_pred=m*x+c
    r=y-y_pred
    m_grad=(-2/n)*sum(x*r)
    x_grad=(-2/n)*sum(r)
    m -= lr*m_grad
    c -= lr*x_grad


print(f"Slope (m): {m:.4f}")
print(f"Intercept (c): {c:.4f}")