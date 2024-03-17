import turtle

def draw_tree(branch_length, t, level):
    if level > 0:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t, level - 1)
        t.left(40)
        draw_tree(branch_length - 15, t, level - 1)
        t.right(20)
        t.backward(branch_length)

def main():
    # Запит рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії (більше 0): "))
    if level <= 0:
        print("Рівень рекурсії має бути більше 0!")
        return

    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_tree(100, t, level)
    window.mainloop()

if __name__ == "__main__":
    main()