"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    a = input('점수를 입려과세요: ')
    if a > 89:
        print('A')
    if 79< a < 90:
        print('B')
    if 69< a < 80:
        print('C')
    if 59 < a <70:
        print('D')
    else:
        print('F')
    return


if __name__ == '__main__':
    main()
