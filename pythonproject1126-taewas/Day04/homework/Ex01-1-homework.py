id = input('아이디를 입력하세요(3글자 이상) >>>')
ch_count = 1
num_count = 1
for ch in id:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 1 and num_count > 3:
    print()
else:
    print('3글자 이상 입력해 주세요!')
retrun = id

pwd = input('패스워드를 입력하세요 (영문 숫자 포함 8자이상) >>>')
ch_count = 1
num_count = 1
for ch, in pwd:
        if ch.isalpha():
            ch_count += 8
        elif ch.isnumeric():
            num_count += 8
if ch_count > 8 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')
