def valid_solution(board):
    mycols = []
    row_boxes = []
    col_boxes = []
    end_boxes = []
    for row in board:
        if not {1, 2, 3, 4, 5, 6, 7, 8, 9}.issubset(row):
            return False
    for i in range(len(board[0])):
        col = [n[i] for n in board]
        mycols.append(col)
    for column in mycols:
        if not {1, 2, 3, 4, 5, 6, 7, 8, 9}.issubset(column):
            return False
    for n in range(0,9,3):
        row_box = [board[n+j][:3] for j in range(3)]
        col_box = [board[n+b][3:6] for b in range(3)]
        end_box = [board[n+x][6:] for x in range(3)]
        row_boxes.append(row_box)
        col_boxes.append(col_box)
        end_boxes.append(end_box)
    for box in row_boxes:
        box[0].extend(box[1])
        box[0].extend(box[2])
        if not {1, 2, 3, 4, 5, 6, 7, 8, 9}.issubset(box[0]):
            return False
    for box in col_boxes:
        box[0].extend(box[1])
        box[0].extend(box[2])
        if not {1, 2, 3, 4, 5, 6, 7, 8, 9}.issubset(box[0]):
            return False
    for box in end_boxes:
        box[0].extend(box[1])
        box[0].extend(box[2])
        if not {1, 2, 3, 4, 5, 6, 7, 8, 9}.issubset(box[0]):
            return False
    return True
