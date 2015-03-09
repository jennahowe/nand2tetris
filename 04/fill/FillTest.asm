@R0
D=M   //load R0 location into D register
@8192
D=A   //set value at R0 to 8192
(loop)
    @R0
    D=M-1   //decrement counter in R0
    @SCREEN
    D=D+A   //add screen address to decremented counter so now D has the address
            //of the thing you want to change

    D=A
    M=-1

    @R0
    D=M
    @loop
    D;JNE

(end)
@end
0;JMP
