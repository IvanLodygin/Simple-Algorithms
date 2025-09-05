from modules.rabin_karp import search_patterns
from modules.graham import graham
from modules.drawer import visualize_convex_hull

pattern = input()
text = input()
result = search_patterns(pattern, text)
print(*result)

quantity = int(input())
dots = list()

for _ in range(quantity):
	dots.append(list(map(int, input().split(","))))

hull, area = graham(dots)
print(hull, area)

visualize_convex_hull(dots, hull, area)