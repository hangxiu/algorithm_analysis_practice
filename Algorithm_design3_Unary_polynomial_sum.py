# 求解 x**6 - 6x**4 + x**3 + 12x + 3**0.5

def Polynomial(x):
    return x**6 - 6*(x**4) + x**3 + 12*x + 3**(0.5)

def Polynomial_derivation(x):
    return 6*(x**5) - 24*(x**3) + 2*(x**2) + 12


# 牛顿迭代法，牛顿迭代法是从泰勒公式中取前两项构成线性近似方程，从x0开始，一步一步接近近似解，直到误差在限定范围内。
# if __name__ == "__main__":
#     x1 = 6
#     x0 = 0
#     while abs(x1 - x0) >= 1e-9:
#         x0 = x1
#         x1 = x0 - Polynomial(x0) / Polynomial_derivation(x0)
#     print("root 为：%g" %x1)
#     print("test 为：%g" %Polynomial(x1))
    # root 为：-0.143876
    # test 为：-7.4829e-14
    # 真实解为： -2.3115909，  -0.14394663


#   二分法求方程的解
if __name__ == "__main__":
    x0 = -1
    x1 = 1
    root = 3
    while abs(x0 - x1) >= 1e-11:
        mid = (x0 + x1) / 2
        if Polynomial(mid) == 0:
            root = mid
            break
        elif Polynomial(x0) * Polynomial(mid) < 0:
            x1 = mid
        elif Polynomial(x1) * Polynomial(mid) < 0:
            x0 = mid
    print("root 为：%g" %((x1+x0) / 2))
    print("test 为：%g" %Polynomial((x0+x1) / 2))

    x0 = -9
    x1 = -1
    root = 3
    while abs(x0 - x1) >= 1e-11:
        mid = (x0 + x1) / 2
        if Polynomial(mid) == 0:
            root = mid
            break
        elif Polynomial(x0) * Polynomial(mid) < 0:
            x1 = mid
        elif Polynomial(x1) * Polynomial(mid) < 0:
            x0 = mid
    print("root 为：%g" %((x1+x0) / 2))
    print("test 为：%g" %Polynomial((x0+x1) / 2))
    
    # root 为：-0.143876
    # test 为：-7.07767e-12
    # root 为：-2.64421
    # test 为：8.46376e-10
