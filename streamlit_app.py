{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/CsyNgv1K0G1+rDNlmzzO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ganyiwatakunda/ObjectDetection/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PiWK_o5TEP7Y",
        "outputId": "08952428-7d94-4ff1-efc6-38ca5851133b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 10.3 MB 5.7 MB/s \n",
            "\u001b[K     |████████████████████████████████| 164 kB 58.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 45.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 78 kB 6.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 237 kB 45.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 182 kB 53.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 63 kB 1.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 51 kB 6.5 MB/s \n",
            "\u001b[?25h  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ca0zr6EqK4Qf",
        "outputId": "c581025c-8cdc-4ba7-afe8-3e17477e6160"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing streamlit_app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile streamlit_app.py \n",
        "import streamlit as st \n",
        "st.markdown(\"\"\" This is a Streamlit App \"\"\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit_option_menu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vBGvMD9zv9Wj",
        "outputId": "472e4d00-028e-49e2-c5e7-9b4b3ce8299c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit_option_menu\n",
            "  Downloading streamlit_option_menu-0.3.2-py3-none-any.whl (712 kB)\n",
            "\u001b[K     |████████████████████████████████| 712 kB 5.0 MB/s \n",
            "\u001b[?25hRequirement already satisfied: streamlit>=0.63 in /usr/local/lib/python3.7/dist-packages (from streamlit_option_menu) (1.15.1)\n",
            "Requirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (4.2.0)\n",
            "Requirement already satisfied: semver in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (2.13.0)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (0.8.0)\n",
            "Requirement already satisfied: validators>=0.2 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (0.20.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (3.1.29)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (3.19.6)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (1.5.1)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (1.3.5)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (6.0.4)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (5.2.0)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (7.1.2)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (9.0.0)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (4.13.0)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (2.23.0)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (2.8.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (4.1.1)\n",
            "Requirement already satisfied: pympler>=0.9 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (1.0.1)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (21.3)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (7.1.2)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (12.6.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (1.21.6)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (0.10.2)\n",
            "Requirement already satisfied: blinker>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (1.5)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.7/dist-packages (from streamlit>=0.63->streamlit_option_menu) (2.1.9)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (0.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (0.12.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (2.11.3)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.7/dist-packages (from gitpython!=3.1.19->streamlit>=0.63->streamlit_option_menu) (4.0.9)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit>=0.63->streamlit_option_menu) (5.0.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=1.4->streamlit>=0.63->streamlit_option_menu) (3.10.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (5.10.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (0.19.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (22.1.0)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging>=14.1->streamlit>=0.63->streamlit_option_menu) (3.0.9)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit>=0.63->streamlit_option_menu) (2022.6)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit>=0.63->streamlit_option_menu) (2.0.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil->streamlit>=0.63->streamlit_option_menu) (1.15.0)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_option_menu) (3.0.4)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_option_menu) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_option_menu) (2022.9.24)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_option_menu) (2.10)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in /usr/local/lib/python3.7/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_option_menu) (2.6.1)\n",
            "Requirement already satisfied: commonmark<0.10.0,>=0.9.0 in /usr/local/lib/python3.7/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_option_menu) (0.9.1)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.7/dist-packages (from validators>=0.2->streamlit>=0.63->streamlit_option_menu) (4.4.2)\n",
            "Installing collected packages: streamlit-option-menu\n",
            "Successfully installed streamlit-option-menu-0.3.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LudVep9Xg4VX"
      },
      "outputs": [],
      "source": [
        "\n",
        "\n",
        "import streamlit as st\n",
        "import cv2\n",
        "import tensorflow as tf \n",
        "import numpy as np\n",
        "from keras.models import load_model\n",
        "import sys\n",
        "from streamlit_option_menu import option_menu\n",
        "\n",
        "#Loading the Inception model\n",
        "model= load_model('./model.h5',compile=(False))\n",
        "st.markdown('<style>body{background-color:Blue;}</style>',unsafe_allow_html=True)\n",
        "\n",
        "\n",
        "#Functions\n",
        "def predict(frame, model):\n",
        "    # Pre-process the image for model prediction\n",
        "    img = cv2.resize(frame, (299, 299))\n",
        "    img = img.astype(np.float32)\n",
        "    img = np.expand_dims(img, axis=0)\n",
        "\n",
        "    img /= 255.0\n",
        "\n",
        "    # Predict with the Inceptionv3 model\n",
        "    prediction = model.predict(img)\n",
        "\n",
        "    # Convert the prediction into text\n",
        "    pred_text = tf.keras.applications.inception_v3.decode_predictions(prediction, top=1)\n",
        "    for (i, (imagenetID, label, prob)) in enumerate(pred_text[0]):\n",
        "        label = (\"{}: {:.2f}%\".format(label, prob * 100))\n",
        "\n",
        "    st.markdown(label)\n",
        "\n",
        "\n",
        "def predict2(frame, model):\n",
        "    # Pre-process the image for model prediction\n",
        "    img = cv2.resize(frame, (299, 299))\n",
        "    img = img.astype(np.float32)\n",
        "    img = np.expand_dims(img, axis=0)\n",
        "\n",
        "    img /= 255.0\n",
        "\n",
        "    # Predict with the Inceptionv3 model\n",
        "    prediction = model.predict(img)\n",
        "\n",
        "    # Convert the prediction into text\n",
        "    pred_text = tf.keras.applications.inception_v3.decode_predictions(prediction, top=1)\n",
        "    for (i, (imagenetID, label, prob)) in enumerate(pred_text[0]):\n",
        "        pred_class = label\n",
        "       \n",
        "\n",
        "    return pred_class\n",
        "\n",
        "def object_detection(search_key,frame, model):\n",
        "    label = predict2(frame,model)\n",
        "    label = label.lower()\n",
        "    try:\n",
        "        if label.find(search_key) > -1:\n",
        "            sys.exit( st.image(frame, caption=label))\n",
        "        else:\n",
        "            pass  \n",
        "           \n",
        "\n",
        "    except:\n",
        "        print('')\n",
        "            \n",
        "            \n",
        "        \n",
        "\n",
        "\n",
        "\n",
        "# Main App\n",
        "def main():\n",
        "    \n",
        "    st.title(\"***Real Time Object Detection***\")\n",
        "    st.text(\"Machine Learning\")\n",
        "\n",
        "    \n",
        "    choice = option_menu(\"Main Menu\",[\"Home\",\"Upload\",\"About\"],icons = [\"house\",\"cloud_upload\",\"list-task\"],menu_icon =\"cast\",default_index = 0,orientation = \"horizontal\")\n",
        "    \n",
        "    if choice == \"Upload\":\n",
        "        st.subheader(\"Upload Your Video\")\n",
        "\n",
        "        video_file_path = st.file_uploader(\"accepting mp4,avi\", type=[\"mp4\", \"avi\"])\n",
        "\n",
        "        if video_file_path is not None:\n",
        "            path = video_file_path.name\n",
        "            with open(path,mode='wb') as f: \n",
        "                f.write(video_file_path.read())         \n",
        "                st.success(\"File Uploaded\")\n",
        "            cap = cv2.VideoCapture(path)\n",
        "            frame_width = int(cap.get(3))\n",
        "            frame_height = int(cap.get(4))\n",
        "\n",
        "            fourcc = cv2.VideoWriter_fourcc(*'XVID')\n",
        "            output = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))\n",
        "            \n",
        "            if st.button(\"Detect Objects\"):\n",
        "                \n",
        "                # Start the video prediction loop\n",
        "                while cap.isOpened():\n",
        "                    ret, frame = cap.read()\n",
        "    \n",
        "                    if not ret:\n",
        "                        break\n",
        "    \n",
        "                    \n",
        "                    predict(frame, model)\n",
        "    \n",
        "                    # Display the resulting frame\n",
        "                    \n",
        "                cap.release()\n",
        "                output.release()\n",
        "                cv2.destroyAllWindows()\n",
        "                \n",
        "            key = st.text_input('Search key')\n",
        "            key = key.lower()\n",
        "            \n",
        "            if key is not None:\n",
        "            \n",
        "                if st.button(\"Search for an object\"):\n",
        "                    \n",
        "                    \n",
        "                    # Start the video prediction loop\n",
        "                    while cap.isOpened():\n",
        "                        ret, frame = cap.read()\n",
        "        \n",
        "                        if not ret:\n",
        "                            break\n",
        "        \n",
        "                        # Perform object detection\n",
        "                        object_detection(key,frame, model)\n",
        "                        \n",
        "                    cap.release()\n",
        "                    output.release()\n",
        "                    cv2.destroyAllWindows()\n",
        "\n",
        "    \n",
        "        \n",
        "       \n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wTvOpRPRvP0a"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}