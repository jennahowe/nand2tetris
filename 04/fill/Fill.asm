// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

//entire program loops to continously check the keyboard
(loop)
    @KBD
    D=M          //load the value at @KBD into D
    @whitescreen
    D;JEQ
    @blackscreen
    D;JNE        //if a button is being pressed jump to (blackscreen)

    @loop
    0;JMP

    (blackscreen)
        @SCREEN
        D=M      //load value of first 32px of screen into D
        @loop
        D;JNE    //if first 32px are black jump back to the beginning

        @R0
        M=0

        (blackscreenloop)
            @R0
            D=M    //load the value at R0 into D

            @R0
            M=M+1

            @KBD
            D=A-D   
            A=D
            M=-1

            @SCREEN
            D=D-A

            @blackscreenloop
            D;JNE    //if D!=0 jump to (screenloop)
            @loop
            D;JEQ  //if value at D==0 go back to beginning

    (whitescreen)
        @SCREEN
        D=M      //load value of first 32px of screen into D
        @loop
        D;JEQ    //if first 32px are black jump back to the beginning

        @R0
        M=0

        (whitescreenloop)
            @R0
            D=M    //load the value at R0 into D

            @R0
            M=M+1

            @KBD
            D=A-D   
            A=D
            M=0

            @SCREEN
            D=D-A

            @whitescreenloop
            D;JNE    //if D!=0 jump to (whitescreenloop)
            @loop
            D;JEQ  //if value at D==0 go back to beginning

    @loop
    0;JMP



