# Асуулт
# дараах тэмдэгтүүдээс бүрдсэн s мөр өгөгдсөн:
# (, ), *

# Энэ мөр нь дараах нөхцөлүүдийг хангасан эсэхийг шалгана :

# Бүх нээлттэй хаалт ( хаалттай ) болж таарах ёстой.
# * тэмдэгт нь дараах гурван утгын аль нэгийг илэрхийлж болно:
#     Нээлттэй хаалт (.
#     Хаалттай хаалт ).
#     Хоосон тэмдэгт.
#output: true, false


def checkValidString(s: str) -> bool:
    minOpen = 0
    maxOpen = 0

    for char in s:
        if char == '(':
            minOpen += 1
            maxOpen += 1
        elif char == ')':
            minOpen = max(minOpen - 1, 0)
            maxOpen -= 1
        else:  # char == '*'
            minOpen = max(minOpen - 1, 0)
            maxOpen += 1

        if maxOpen < 0:
            return False

    return minOpen == 0
