from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# โหลดโมเดล
model = joblib.load('model.pkl')  # เปลี่ยนชื่อไฟล์เป็นชื่อไฟล์โมเดลที่คุณมี เช่น model.joblib

# Route สำหรับหน้าเว็บหลัก
@app.route('/')
def home():
    return render_template('index.html')  # แสดงไฟล์ HTML ของคุณ เช่น index.html

# Route สำหรับการ predict
@app.route('/predict', methods=['POST'])
def predict():
    # รับค่าจากฟอร์มที่ส่งมาจาก HTML
    data = request.form

    # สร้างข้อมูล input ที่จะใช้ predict
    input_data = [
        float(data['bmi']),
        int(data['diabetes']),
        int(data['physActivity']),
        int(data['fruits']),
        int(data['genHlth']),
        int(data['mentHlth']),
        int(data['physHlth']),
        int(data['age']),
        int(data['education']),
        int(data['income'])
    ]

    # ทำนายผล
    prediction = model.predict([input_data])[0]

    # ส่งผลลัพธ์กลับไปที่ HTML
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
