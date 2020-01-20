# 导入人脸识别库
import face_recognition


def compare_face(image01, image02):
    known_image = face_recognition.load_image_file(image01)
    unknown_image = face_recognition.load_image_file(image02)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[1]
    distance = face_recognition.compare_faces(
        [known_encoding], unknown_encoding)
    return distance


print(compare_face('jay.png', 'pic.png'))
