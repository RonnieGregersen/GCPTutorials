#STEP 2:
# from google.cloud import pubsub_v1



#STEP 1:
from flask import Flask, render_template, request, jsonify

#STEP 2:
# project_id = "devodk-platform-prod"
# topic_id = "nyttopic"

#STEP 1
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/webshop')
def webshop():
    return render_template('webshop.html')

#STEP 2: 
# @app.route('/call_function', methods=['POST'])
# def call_function():
#     data = request.get_json()
#     name = str(data['name'])
#     organization = str(data['organization'])

#     # Your Python function
#     print("kalder funktionen")
#     result = pubsubpublisher(name, organization)

#     return jsonify(result=result)

# def pubsubpublisher(name, organization):
#     publisher = pubsub_v1.PublisherClient()
#     topic_path = publisher.topic_path(project_id, topic_id)

#     for n in range(1, 10):
#         data_str = f"{name}, {organization}"
#         # Data must be a bytestring
#         data = data_str.encode("utf-8")
#         # Add two attributes, origin and username, to the message
#         future = publisher.publish(
#             topic_path, data, navn=name, organisation=organization
#         )
#         print(future.result())
#         returnstring = f"Velkommen til {name} - Din besked er sendt til pubsub"
#         return returnstring

#STEP 1
if __name__ == '__main__':
    app.run(debug=True)