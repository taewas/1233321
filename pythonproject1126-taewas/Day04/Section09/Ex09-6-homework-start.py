id = int(input('아이디를 입력하세요(3글자 이상) >>>'))
ch_count = 0
num_count = 0
for ch in id:
    if ch.isalpha():
        ch_count += 3
    elif ch.isnumeric():
        num_count += 3

if ch_count > 0 and num_count > 0:
    print()
else:
    print('3글자 이상 입력해 주세요!')


pwd = input('패스워드를 입력하세요 (영문 숫자 포함 8자이상) >>>')
ch_count = 0
num_count = 0
for ch, in pwd:
        if ch.isalpha():
            ch_count += 8
        elif ch.isnumeric():
            num_count += 8
if ch_count > 8 and num_count > 8:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')

x = input('패스워드 확인 한번 더 입력하세요 >>>')
print(x)


