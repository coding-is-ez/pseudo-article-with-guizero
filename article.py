from guizero import App, Text, Picture, Box

# Main app
window = App(title = "Random article")

# Text
title = Text(window, text = "Liverpool thua Chelsea phút bù ở Ngoại hạng Anh", bold = True, size = 25)

aritcle_box = Box(window, width = "fill")
first_paragraph = Text(aritcle_box, text = """ Liverpool đã để thua Chelsea 0-1 ở vòng 34 Ngoại hạng Anh trên sân Anfield.
                                            Trận thua này khiến Liverpool bị bỏ lại trong cuộc đua vô địch khi kém đội đầu""", size = 15)

pic = Picture(window, image = "forsakenedfkingimage.png")

second_paragraph = Text(aritcle_box, text = """ đầu bảng Manchester City 1 điểm và thi đấu nhiều hơn một trận.
                                    Trận đấu diễn ra hấp dẫn ngay từ những phút đầu tiên khi cả hai đội đều...""", size = 15)

# Display the app
window.display()