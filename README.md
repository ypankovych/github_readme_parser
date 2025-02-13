# Internal GitHub team readme parser

## Running

```bash
docker build -t gh-readme-parser .
docker run -p 5431:5000 gh-readme-parser
```

## Usage

Do a `GET` request to `http://0.0.0.0:5431/readme/<team_name>`

### Response

#### Success:
```json
{
  "readme": "Test readme\nblah blah\n"
}
```
#### Error:
```json
{
  "error": "Team not found"
}
```