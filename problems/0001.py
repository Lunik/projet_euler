
def solution(limit):
  result = 0

  for i in range(limit):
    if i%3 == 0 or i%5 == 0:
      result += i

  return result


if __name__ == "__main__":
  print(solution(1000))