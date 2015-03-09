//@R0
//D=M   //load R0 location into D register


//@16388
//D=A+1   
//A=D
//M=-1

//@SCREEN
//M=-1

//(end)
//@end
//0;JMP



@R0
D=M   //load R0 location into D register
@8192
D=A

@SCREEN
D=A+D   
A=D
M=-1

(end)
@end
0;JMP

