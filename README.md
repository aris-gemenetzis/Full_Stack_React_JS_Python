# Full Stack Dev
Full Stack Mock App in React JS & Python FastAPI with OpenAI Integration

## Installation
---------
### Frontend
- Install [React JS] (https://react.dev/)
- `cd front`
- `npm install`
- `npm start`

or alternatively build and deploy Docker Image using provided Dockerfile:
```bash
cd front
docker build -t <frontend> .
docker run -p 3000:3000 <frontend>
```
### Backend
- Install [Python] (https://www.python.org/downloads/)
- `cd back`
- `pip install -r requirements.txt`
- `python main.py`

or alternatively build and deploy Docker Image using provided Dockerfile:
```bash
cd back
docker build -t <backend> .
docker run -p 8000:8000 <backend>
```
## Usage
---------
Run Backend first using `python main.py` then Frontend with `npm start`. Enter appropriate values in the client form fields and wait for server response to display on screen.

**Note:** For testing purposes, Frontend operates in a PUSH/POP Stack fashion for **Update** and **Delete** options using a `counter` variable. Making sure both Frontend and Backend are in sync is therefore critical for the program to run smoothly.

## Implementation details
---------
### Frontend
- `App.js`: displays `TaxForm.jsx`
- `TaxForm.jsx`: contains form code
- `MarkdownPreview.js`: used by `TaxForm.jsx` to display OpenAI response on screen
- `App.test.js`: test code for displaying `App.js`

### Backend
- `main.py`: used to call `api.py`
- `api.py`: contains Backend code, including OpenAI call
- `tester.py`: test code containing a variety of calls to server

## Docker Instructions
---------
Build and deploy Docker images using the corresponding Dockerfiles.

### Frontend
```bash
cd front
docker build -t <frontend> .
docker run -p 3000:3000 <frontend>
```
### Backend
```bash
cd back
docker build -t <backend> .
docker run -p 8000:8000 <backend>
```

## CI Pipeline
---------
### Frontend
A modified version of the standard GitHub Node.js workflow is used to establish a CI Frontend Pipeline. It runs tests on each push (and pull request) to the main branch, and ensures that Frontend code is functional by running a typical display test according to `App.test.js`. Necessary edits have been made in terms of library dependencies and working path definitions. The exact configuration can be found in `.github/workflows/node_js.yml`.
