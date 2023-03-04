# PDF_AUTOFILL

clone repo

```
git clone https://github.com/PraveenKusuluri08/PDF_AUTOFILL.git
```
Navigate to directory
```
cd PDF_AUTOFILL
```

After cloning the repo need to install packages for that,

```
pip install -r requirements.txt
```
After installing packages,

```
python app.py
```

app runs with the port specified 
<hr/>
<h1>Requirements to run this project</h1>

1) python version 3.10
2) postman or Thunder Client in vscode
3) pdf file.


<h5>How to hit endpoints<h5>
<p>Total there are 3 end points for the pdf</p>

→ **Getting all fields from the pdf**
```
curl --location 'http://localhost:8000/get_fields' \
--header 'Auth: Token' \
--form 'file=@"<actual location of the pdf file>"'
```

<hr/>

→ Update single from the pdf
```
curl --location --request PUT 'http://localhost:8080/update_field' \
--form 'file=@"<actual location of the pdf file>"' \
--form 'field="{\"Pt1Line2a_GivenName[0]\":\"Praveen\"}"'
```

<hr/>

→ Update multiple fields from the pdf
```
curl --location --request PUT 'http://localhost:8080/update_fields' \
--form 'file=@"<actual location of the pdf file>"' \
--form 'fields="[{\"Pt1Line2a_FamilyName[0]\":\"Praveen\"},{\"Pt3Line5c_MiddleName[0]\":\"praveen\"},{\"Pt3Line5c_MiddleName[1]\":\"Sai\"},{\"Pt3Line8_USCISOnlineAcctNumber[0]\":\"123456789123\"},{\"Line3d_State[0]\":\"NV\"}]"'
```
