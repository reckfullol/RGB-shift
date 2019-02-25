import cv2
import numpy as np

if __name__ == "__main__":
    picture_path = "../pictures/Neon-Genesis-Evangelion-on-Netflix.png"

    picture = cv2.imread(picture_path, True)

    rows, cols, _ = picture.shape
    green, red, blue = cv2.split(picture)

    # must be positive
    offset_x = 10
    offset_y = 10

    '''
    OffsetMatrix = [1 0 tx]
                   [0 1 ty]
    '''
    offset_matrix_green = np.float32([
        [1, 0, offset_x],
        [0, 1, offset_y]
    ])

    offset_matrix_blue = np.float32([
        [1, 0, -offset_x],
        [0, 1, -offset_y]
    ])

    # shift
    green = cv2.warpAffine(green, offset_matrix_green, (cols, rows))
    blue = cv2.warpAffine(blue, offset_matrix_blue, (cols, rows))

    # merge RGB channel
    merged = cv2.merge([green, red, blue])

    # cut out
    merged = merged[offset_y:rows-offset_y, offset_x:cols-offset_x]

    # display
    cv2.imshow("native", picture)
    cv2.imshow("blue", blue)
    cv2.imshow("red", red)
    cv2.imshow("green", green)
    cv2.imshow("merged", merged)
    cv2.imwrite("../pictures/native.png", picture)
    cv2.imwrite("../pictures/blue.png", blue)
    cv2.imwrite("../pictures/red.png", red)
    cv2.imwrite("../pictures/green.png", green)
    cv2.imwrite("../pictures/merged.png", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
