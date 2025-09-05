import matplotlib.pyplot as plt

def visualize_convex_hull(points, convex_hull, convex_area):
    plt.figure(figsize=(8, 6))
    
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, color="blue", label="Точки")
    
    plt.annotate("Start", points[0], xytext=(6, -10), textcoords="offset points",
                 color="red", ha="center")
    
    for idx in range(len(convex_hull)):
        next_idx = (idx + 1) % len(convex_hull)
        plt.plot(
            [convex_hull[idx][0], convex_hull[next_idx][0]],
            [convex_hull[idx][1], convex_hull[next_idx][1]],
            color="red", label="Граница оболочки" if idx == 0 else ""
        )

    plt.title(f"Визуализация выпуклой оболочки\nПлощадь: {convex_area}")
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    
    plt.legend()
    plt.grid(visible=True)
    
    plt.show()
