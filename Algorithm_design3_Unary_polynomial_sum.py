# 求解 x**6 - 6x**4 + x**3 + 12x + 3**0.5

def Polynomial(x):
    return x**6 - 6*(x**4) + x**3 + 12*x + 3**(0.5)

def Polynomial_derivation(x):
    return 6*(x**5) - 24*(x**3) + 2*(x**2) + 12


# 牛顿迭代法，牛顿迭代法是从泰勒公式中取前两项构成线性近似方程，从x0开始，一步一步接近近似解，直到误差在限定范围内。
#  方法步骤
# 以一元非线性方程 f(x)=0 为例，对函数 f(x)进行Taylor级数展开（只展开至线性项）得  
#    f(x) = f(x0)+f'(x0)(x-x0)       所以方程可写成       
# f(x0)+f'(x0)(x-x0) = 0        
# 其中x0是给定的已知值，则不难推导出方程的解（当然，只是近似解，毕竟Taylor展开过程中只取了线性项） 
# x = x0 - f(x0) / f'(x0)   其中x不是真实解，但是相比之前的x0更靠近真实解了，
# 因此可以多重复几次上述过程，从而使得到的解非常接近准确值。所以，对于一元非线性方程，
# 牛顿拉夫逊迭代公式为：      x(k+1) = x(k) - f(x(k)) / f'(x(k))
if __name__ == "__main__":
    x1 = -0.1440
    x0 = 1
    while abs(x1 - x0) >= 1e-9:
        x0 = x1
        x1 = x0 - Polynomial(x0) / Polynomial_derivation(x0)
    print("root 为：%g" %x1)
    print("test 为：%g" %Polynomial(x1))

    x1 = -3
    x0 = 0
    while abs(x1 - x0) >= 1e-9:
        x0 = x1
        x1 = x0 - Polynomial(x0) / Polynomial_derivation(x0)
    print("root 为：%g" %x1)
    print("test 为：%g" %Polynomial(x1))
    # root 为：-0.143876
    # test 为：-4.66294e-14
    # root 为：-2.64421
    # test 为：2.27339e-09
    # 真实解为： -2.3115909，  -0.14394663


#   二分法求方程的解
#   方法步骤
# 1
# 如果要求已知函数 f(x) = 0 的根 (x 的解)，那么
# 2
# 先要找出一个区间 [a, b]，使得f(a)与f(b)异号。
# 根据介值定理，这个区间内一定包含着方程式的根。
# 3
# 求该区间的中点m=(a+b)/2，并找出 f(m) 的值。
# 4
# 若 f(m) 与 f(a) 正负号相同，则取 [m, b] 为新的区间, 否则取 [a, m]。
# 5
# 重复第3步和第4步，直到得到理想的精确度为止


# if __name__ == "__main__":
#     x0 = -1
#     x1 = 0
#     root = 3
#     while abs(x0 - x1) >= 1e-11:
#         mid = (x0 + x1) / 2
#         if Polynomial(mid) == 0:
#             root = mid
#             break
#         elif Polynomial(x0) * Polynomial(mid) < 0:
#             x1 = mid
#         elif Polynomial(x1) * Polynomial(mid) < 0:
#             x0 = mid
#     print("root 为：%g" %((x1+x0) / 2))
#     print("test 为：%g" %Polynomial((x0+x1) / 2))

#     x0 = -3
#     x1 = -1
#     root = 3
#     while abs(x0 - x1) >= 1e-11:
#         mid = (x0 + x1) / 2
#         if Polynomial(mid) == 0:
#             root = mid
#             break
#         elif Polynomial(x0) * Polynomial(mid) < 0:
#             x1 = mid
#         elif Polynomial(x1) * Polynomial(mid) < 0:
#             x0 = mid
#     print("root 为：%g" %((x1+x0) / 2))
#     print("test 为：%g" %Polynomial((x0+x1) / 2))
    
    # root 为：-0.143876
    # test 为：-7.07767e-12
    # root 为：-2.64421
    # test 为：8.46376e-10

    # 真实解为： -2.3115909，  -0.14394663

