"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    a = input('나이를 입력하세요: ')
    b = input('키를 입력하세요:')
    if a < 14 or b < 160:
        print('O')
    if a > 13 or b>=160:
        print('X')
    return


if __name__ == '__main__':
    main()
