# Асуулт
# Танд дөрвөн оронтой битүү түгжээ өгөгдсөн бөгөөд тус бүрийн орон 0-9 хооронд утга агуулдаг. 
# Харамсалтай нь хэд хэдэн "тогтмол" орон байгаа бөгөөд та түгжээг онгойлгохын тулд тэдгээрийг эргүүлэх хэрэгтэй.
# Тодорхойлолт:
# Хамгийн бага алхмуудыг тооцоолж, эхний "0000" комбинациас түлхүүрийг хэрхэн онгойлгохыг олоорой. Хэрэв энэ боломжгүй бол -1-г буцаана уу.

from collections import deque 

def openLock(deadends, target):
    dead = set(deadends)  # deadends жагсаалтыг set болгон хөрвүүлнэ, ингэснээр цаг хугацааны хэмнэлт гарна.
    
    # Хэрвээ "0000" нь deadends-д байгаа бол шууд -1 буцаах
    if "0000" in dead:
        return -1
    
    queue = deque([("0000", 0)])  # queue-д эхлэлийн "0000" ба 0 алхам оруулна
    visited = set(["0000"])  # "0000"-г орсон гэж тэмдэглэх

    while queue:
        current, steps = queue.popleft()  # queue-оос хамгийн анхны элементийг авна
        
        # Хэрвээ хүрсэн combination нь target байвал алхамын тоог буцаана
        if current == target:
            return steps 
        
        # Бүх боломжит хөдөлгөөнүүдийг турших
        for i in range(4): 
            digit = int(current[i]) 
            
            for move in [-1, 1]:  # Орлогдсон оронд тоо өсгөх эсвэл бууруулах
                new_digit = (digit + move) % 10  # Тоо өсгөж эсвэл бууруулах, 10-р хязгаарлалтад оруулна
                new_combination = current[:i] + str(new_digit) + current[i+1:]  # Шинэ комбинаци гаргана
                
                # Хэрвээ шинэ комбинаци deadend-д ороогүй бөгөөд өмнө нь орж байгаагүй бол
                if new_combination not in dead and new_combination not in visited:
                    visited.add(new_combination)  # Шинэ комбинацийг орж байгааг тэмдэглэнэ
                    queue.append((new_combination, steps + 1))  # Шинэ комбинацийг queue-д оруулна
        
    # Хэрвээ бүх боломжит комбинацуудыг шалгаж дууссан ч target олдохгүй бол -1 буцаана
    return -1
