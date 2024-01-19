import cv2
import dlib
import argparse
# Загрузка предобученных моделей для распознавания лиц
detector = dlib.get_frontal_face_detector()

# Загрузка видеофайла по умолчанию
video_path = '1.mp4'
def process_video(video_path=video_path):
    video = cv2.VideoCapture(video_path)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4')
    out = cv2.VideoWriter('output.mp4', -1, 20.0, (640, 480))
    # count_picture = 0
    while True:
        # Считывание текущего кадра
        ret, frame = video.read()

        if not ret:
            # print('Wrong path')
            break

        # Преобразование кадра в черно-белое изображение
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Распознавание лиц на кадре
        faces = detector(gray)
        # count_picture +=1
        # Отрисовка прямоугольников вокруг лиц
        for face in faces:
            x, y = face.left(), face.top()
            w, h = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)

        # Вывод кадра с отрисованными прямоугольниками
        cv2.imshow('Video', frame)
        out.write(frame)

        # Выход из цикла по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # print(count_picture)
    # Освобождение ресурсов
    video.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video processing')
    parser.add_argument('--video', help='Path to the video file')
    args = parser.parse_args()

    process_video(args.video)


# Запуск через командную строку: python test.py --video 1.mp4