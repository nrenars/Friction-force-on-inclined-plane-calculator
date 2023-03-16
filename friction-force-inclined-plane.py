def drawing():
    print("""
                            a = ?
                            m = ?
       Fr      *   Fv   *   μ = ?
            *    *    * *   Fv = ?
         *         *    *   
           *    *       *   calculate:
      Fb     *   Fsm    *   Fb = ?
          *             *   Frez = ?    
       * a              *   a = ? 
    *********************   
    """)

def Fsm(x,y):
    return x * y

def FsmX(x,y):
    return round(x * y,2)

def FsmY(x,y):
    return round(x * y,2)

def Fr():
    return FsmY_answer

def Fb(x,y):
    return FsmY_answer * μ

def Frez(x,y,z):
    return x-y-z

def a():
    return Frez_answer / mass

g = 10

while True:
    drawing()
    print('\nWhat are known values? (Press 000 to exit)')
    mass = float(input('What is the value of mass? '))

    if mass == 000:
        break

    μ = float(input('What is the value of friction coefficient? '))
    angle = int(input('How many degree angle? '))
    Fv = (input('What is the value of Fv? '))
    
    class sincos():
        if angle == 1:
            sin = 0.0174  
            cos = 0.9998
        elif angle == 2:
            sin = 0.0349
            cos = 0.9994
        elif angle == 3:
            sin = 0.0523
            cos = 0.9986
        elif angle == 4:
            sin = 0.0698
            cos = 0.9976
        elif angle == 5:
            sin = 0.0872
            cos = 0.9962
        elif angle == 6:
            sin = 0.1045
            cos = 0.9945
        elif angle == 7:
            sin = 0.1219
            cos = 0.9926
        elif angle == 8:
            sin = 0.1392
            cos = 0.9903
        elif angle == 9:
            sin = 0.1564
            cos = 0.9877
        elif angle == 10:
            sin = 0.1736
            cos = 0.9848
        elif angle == 11:
            sin = 0.1908
            cos = 0.9816
        elif angle == 12:
            sin = 0.2079
            cos = 0.9781
        elif angle == 13:
            sin = 0.2249
            cos = 0.9744
        elif angle == 14:
            sin = 0.2419
            cos = 0.9703
        elif angle == 15:
            sin = 0.2588
            cos = 0.9659
        elif angle == 16:
            sin = 0.2756
            cos = 0.9613
        elif angle == 17:
            sin = 0.2924
            cos = 0.9563
        elif angle == 18:
            sin = 0.3090
            cos = 0.9511
        elif angle == 19:
            sin = 0.3256
            cos = 0.9455
        elif angle == 20:
            sin = 0.3420
            cos = 0.9397
        elif angle == 21:
            sin = 0.3584
            cos = 0.9336
        elif angle == 22:
            sin = 0.3746
            cos = 0.9272
        elif angle == 23:
            sin = 0.39077
            cos = 0.9205
        elif angle == 24:
            sin = 0.4067
            cos = 0.9135
        elif angle == 25:
            sin = 0.4336
            cos = 0.9063
        elif angle == 26:
            sin = 0.4384
            cos = 0.8988
        elif angle == 27:
            sin = 0.4540
            cos = 0.8910
        elif angle == 28:
            sin = 0.4695
            cos = 0.8829
        elif angle == 29:
            sin = 0.4848
            cos = 0.8746
        elif angle == 30:
            sin = 0.5
            cos = 0.8660
        elif angle == 31:
            sin = 0.5150
            cos = 0.8571
        elif angle == 32:
            sin = 0.5299
            cos = 0.8480
        elif angle == 33:
            sin = 0.5446
            cos = 0.8387
        elif angle == 34:
            sin = 0.5592
            cos = 0.8290
        elif angle == 35:
            sin = 0.5736
            cos = 0.8191
        elif angle == 36:
            sin = 0.5878
            cos = 0.8090
        elif angle == 37:
            sin = 0.6018
            cos = 0.7986
        elif angle == 38:
            sin = 0.6157
            cos = 0.7880
        elif angle == 39:
            sin = 0.6293
            cos = 0.7772
        elif angle == 40:
            sin = 0.6428
            cos = 0.7660
        elif angle == 41:
            sin = 0.6561
            cos = 0.7547
        elif angle == 42:
            sin = 0.6691
            cos = 0.7431
        elif angle == 43:
            sin = 0.6820
            cos = 0.7314
        elif angle == 44:
            sin = 0.6947
            cos = 0.7193
        elif angle == 45:
            sin = 0.7071
            cos = 0.7071
        elif angle == 46:
            sin = 0.7193
            cos = 0.6947
        elif angle == 47:
            sin = 0.7314
            cos = 0.6820
        elif angle == 48:
            sin = 0.7431
            cos = 0.6691
        elif angle == 49:
            sin = 0.7547
            cos = 0.6561
        elif angle == 50:
            sin = 0.7660
            cos = 0.6428
        elif angle == 51:
            sin = 0.7772
            cos = 0.6293
        elif angle == 52:
            sin = 0.7880
            cos = 0.6157
        elif angle == 53:
            sin = 0.7986
            cos = 0.6018
        elif angle == 54:
            sin = 0.8090
            cos = 0.5878
        elif angle == 55:
            sin = 0.8191
            cos = 0.5736
        elif angle == 56:
            sin = 0.8290
            cos = 0.5592
        elif angle == 57:
            sin = 0.8387
            cos = 0.5446
        elif angle == 58:
            sin = 0.8480
            cos = 0.5299
        elif angle == 59:
            sin = 0.8571
            cos = 0.5150
        elif angle == 60:
            sin = 0.8660
            cos = 0.5000
        elif angle == 61:
            sin = 0.8746
            cos = 0.4848
        elif angle == 62:
            sin = 0.8829
            cos = 0.4695
        elif angle == 63:
            sin = 0.8910
            cos = 0.4540
        elif angle == 64:
            sin = 0.8988
            cos = 0.4384
        elif angle == 65:
            sin = 0.9063
            cos = 0.4226
        elif angle == 66:
            sin = 0.9135
            cos = 0.4067
        elif angle == 67:
            sin = 0.9205
            cos = 0.3907
        elif angle == 68:
            sin = 0.9272
            cos = 0.3746
        elif angle == 69:
            sin = 0.9336
            cos = 0.3584
        elif angle == 70:
            sin = 0.9397
            cos = 0.3420
        elif angle == 71:
            sin = 0.9455
            cos = 0.3256
        elif angle == 72:
            sin = 0.9511
            cos = 0.3090
        elif angle == 73:
            sin = 0.9563
            cos = 0.2924
        elif angle == 74:
            sin = 0.9613
            cos = 0.2756
        elif angle == 75:
            sin = 0.9659
            cos = 0.2588
        elif angle == 76:
            sin = 0.9703
            cos = 0.2419
        elif angle == 77:
            sin = 0.9744
            cos = 0.2249
        elif angle == 78:
            sin = 0.9781
            cos = 0.2079
        elif angle == 79:
            sin = 0.9816
            cos = 0.1908
        elif angle == 80:
            sin = 0.9848
            cos = 0.1736
        elif angle == 81:
            sin = 0.9877
            cos = 0.1564
        elif angle == 82:
            sin = 0.9903
            cos = 0.1392
        elif angle == 83:
            sin = 0.9926
            cos = 0.1219
        elif angle == 84:
            sin = 0.9945
            cos = 0.1045
        elif angle == 85:
            sin = 0.9962
            cos = 0.0872
        elif angle == 86:
            sin = 0.9976
            cos = 0.0698
        elif angle == 87:
            sin = 0.9986
            cos = 0.0523
        elif angle == 88:
            sin = 0.9994
            cos = 0.0349
        elif angle == 89:
            sin = 0.9998
            cos = 0.0174
        elif angle == 90:
            sin = 1
            cos = 0
    sin_cos = sincos()

    Fsm_answer = Fsm(mass,g)
    FsmX_answer = FsmX(Fsm_answer,float(sin_cos.sin))
    FsmY_answer = FsmY(Fsm_answer, float(sin_cos.cos))
    Fr_answer = Fr()
    Fb_answer = Fb(Fr_answer,μ)
    Frez_answer = Frez(Fv, FsmX_answer, Fb_answer) 
    a_answer = a()
    
    print('\nThe value of Fsm is:')
    print(float(mass), '*', int(g), '=', Fsm_answer)

    print('\nThe value of FsmX is:')
    print(float(Fsm_answer), '*', float(sin_cos.sin), '=', FsmX_answer)

    print('\nThe value of FsmY is:')
    print(float(Fsm_answer), '*', float(sin_cos.cos), '=', FsmY_answer)

    print('\nThe value of Fr is:')
    print(FsmY_answer)

    print('\nThe value of Fb is:')
    print(float(Fr_answer), '*', float(μ), '=', Fb_answer)

    print('\nThe value of Frez is:')
    print(float(Fv), '-', float(FsmX_answer), '-', float(Fb_answer), '=', Frez_answer)

    print('\nThe value of a is:')
    print(float(Frez_answer), '/', float(mass), '=', a_answer)