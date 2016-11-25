##210CT LabTasks 2
##Task 3

R = B*C - 2*(B+C)

R1 <- MULT_MATRIX(B,C)
R2 <- ADD(B,C)
R3 <- MULT_SCALAR(R2,2)
R <- R1 - R3

DEF MULT_MATRIX(B,C):
    Ans = B
    for i <- 1 to length R1:
        Ans[i] = B[i] * C[i]
        for j <- 1 to length i:
            Ans[j] = B[j] * C[j]
    return Ans

DEF ADD(B,C):
    Ans = B
    for i <- 1 to length of R2:
        Ans[i] <- B[i] + C[i]
        for j <- 1 to length of i:
            Ans[j] <- B[j] + C[j]
    return Ans

DEF MULT_SCALAR(B,N):
    Ans = B
    for i <- 1 to length of B:
        Ans[i] <- B[i] * N
        for j <- 1 to length of i:
            Ans[j] <- j * N
    return Ans

