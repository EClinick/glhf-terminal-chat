## HOW TO RUN

```pip install -r requirements```

To check what models are available..

```python test.py```

To test it via talking to it in the terminal

```python test-terminal.py```

## API KEY

Create an account with glhf.chat, go to profile, select API settings, and copy API Key and put it in .env following the ```.env.example```

## Example

```bash
Welcome to the Terminal Chat with NVIDIA's Llama-3.1-Nemotron-70B! Type your messages below. Press Ctrl+C to exit.
You: Code a calculator in assembly
AI: Below is a simple implementation of a command-line calculator in x86-64 assembly language using NASM (Netwide Assembler) syntax. This calculator will support basic arithmetic operations: addition, subtraction, multiplication, and division. Please note, for division, we'll only handle unsigned integers to avoid complexity with signed division.

**Calculator in x86-64 Assembly (NASM)**

```nasm
section .data
    msg1 db 'Simple Calculator', 0
    msg2 db '1. Addition', 0
    msg3 db '2. Subtraction', 0
    msg4 db '3. Multiplication', 0
    msg5 db '5. Division (unsigned)', 0
    msg6 db 'Choose an operation (1/2/3/5): ', 0
    msg7 db 'Enter first number: ', 0
    msg8 db 'Enter second number: ', 0
    msg9 db 'Result: ', 0
    msg10 db 'Error! Division by zero.', 0

section .bss
    choice resb 2
    num1 resq 1
    num2 resq 1
    result resq 1

section .text
    global _start

_start:
    ; Display Calculator Message
    mov eax, 4
    mov ebx, 1
    mov ecx, msg1
    mov edx, 17
    int 0x80

    ; Display Menu
    mov eax, 4
    mov ebx, 1
    mov ecx, msg2
    mov edx, 12
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msg3
    mov edx, 15
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msg4
    mov edx, 17
    int 0x80

    mov eax, 4
    mov ebx, 1
    mov ecx, msg5
    mov edx, 22
    int 0x80

    ; Get User Choice
    mov eax, 4
    mov ebx, 1
    mov ecx, msg6
    mov edx, 25
    int 0x80

    mov eax, 3
    mov ebx, 0
    mov ecx, choice
    mov edx, 2
    int 0x80

    ; Get First Number
    mov eax, 4
    mov ebx, 1
    mov ecx, msg7
    mov edx, 17
    int 0x80

    mov eax, 3
    mov ebx, 0
    mov ecx, num1
    mov edx, 10
    int 0x80
    mov eax, [num1]
    sub eax, '0'
    mov [num1], eax

    ; Get Second Number
    mov eax, 4
    mov ebx, 1
    mov ecx, msg8
    mov edx, 18
    int 0x80

    mov eax, 3
    mov ebx, 0
    mov ecx, num2
    mov edx, 10
    int 0x80
    mov eax, [num2]
    sub eax, '0'
    mov [num2], eax

    ; Perform Operation Based on Choice
    mov eax, [choice]
    sub eax, '0'
    cmp eax, 1
    je _add
    cmp eax, 2
    je _sub
    cmp eax, 3
    je _mul
    cmp eax, 5
    je _div
    jmp _exit

_add:
    mov eax, [num1]
    add eax, [num2]
    mov [result], eax
    jmp _display

_sub:
    mov eax, [num1]
    sub eax, [num2]
    mov [result], eax
    jmp _display

_mul:
    mov eax, [num1]
    imul eax, [num2]
    mov [result], eax
    jmp _display

_div:
    mov eax, [num2]
    cmp eax, 0
    je _error
    mov eax, [num1]
    xor edx, edx
    idiv dword [num2]
    mov [result], eax
    jmp _display

_error:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg10
    mov edx, 23
    int 0x80
    jmp _exit

_display:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg9
    mov edx, 9
    int 0x80

    ; Convert result to string (simplified, assumes result fits in a byte)
    mov eax, [result]
    add eax, '0'
    mov [result], eax
    mov eax, 4
    mov ebx, 1
    mov ecx, result
    mov edx, 1
    int 0x80

_exit:
    ; Exit System Call
    mov eax, 1
    xor ebx, ebx
    int 0x80
```

**Compilation and Execution (Linux):**

1. **Assemble and Link:**
   ```bash
   nasm -f elf64 calculator.asm -o calculator.o
   ld calculator.o -o calculator
   ```

2. **Run:**
   ```bash
   ./calculator
   ```

**Note:**
- This code uses system calls which are specific to Linux. If you're on a different platform, the system call numbers and possibly the assembly syntax might differ.
- Error handling is minimal for simplicity. In a real-world application, you'd want to handle more potential errors.
- The division operation only handles unsigned integers and does not check for overflow.
- The result display is simplified and assumes the result can be represented by a single digit (for simplicity). For a more robust solution, you'd implement a function to convert the result to a string, handling multiple digits.
You:
```