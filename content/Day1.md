# लोकल डेवलपमेंट इन्वायरमेंट सेट करना

इससे पहले कि हम वास्तव में Streamlit ऐप्स बनाना शुरू कर सकें, हमें सबसे पहले डेवलपमेंट इन्वायरमेंट को सेट करना होगा.

आइए एक conda इन्वायरमेंट इंस्टॉल और सेट करके शुरू करें.

## **conda इंस्टॉल करना**
- https://docs.conda.io/en/latest/miniconda.html पर जाकर और अपने ऑपरेटिंग सिस्टम (Windows, Mac या Linux) का चयन करके इंस्टॉल करें.
- इंस्टॉल करने के लिए इंस्टॉलर डाउनलोड करें और रन करें.

## **एक नया `conda` इन्वायरमेंट बनाना**
अब जब आपने `conda` इंस्टॉल कर लिया है, तो आइए सभी Python लाइब्रेरी डिपेंडेंसी के प्रबंधन के लिए एक `conda` इन्वायरमेंट बनाएं.

Python 3.9 के साथ एक नया इन्वायरमेंट बनाने के लिए, निम्नलिखित दर्ज करें:

```bash
conda create -n stenv python=3.9
```

जहां `stenv` नाम का एक conda इन्वायरमेंट बनाएगा और `python=3.9` Python वर्ज़न 3.9 वाला conda इन्वायरमेंट इंस्टॉल करेगा.

## **conda इन्वायरमेंट सक्रिय करना**

`stenv` नामक हमारे द्वारा अभी-अभी बनाए गए conda इन्वायरमेंट का उपयोग करने के लिए, कमांड लाइन में निम्नलिखित दर्ज करें:

```bash
conda activate stenv
```

## **Streamlit लाइब्रेरी इंस्टॉल करना**

अब `streamlit` लाइब्रेरी इन्सटॉल करने का समय आ गया है:

```bash
pip install streamlit
```

## **Streamlit डेमो ऐप लॉन्च करना**

Streamlit डेमो ऐप (चित्र 1) लॉन्च करने के लिए, टाइप करें:

```bash
streamlit hello
```
