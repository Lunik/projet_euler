
def solution(limit):
  state = (1, 2)
  result = 0
  new_value = 0

  while state[1] < limit:
    if state[1]%2 == 0:
      result += state[1]

    new_value = state[0] + state[1]
    state = (state[1], new_value)

  return result


if __name__ == "__main__":
  print(solution(4000000))