# Title Cleaner API

A lightweight Flask API that receives blog titles and returns a cleaned, normalized version:
- Removes emojis, accents, and non-English characters
- Keeps punctuation like colons, hyphens, and dashes
- Optimized for filename safety and prompt generation

## Endpoints

- `POST /clean`
  - Body: `{ "title": "Your original title here" }`
  - Response: `{ "cleaned_title": "Your cleaned title" }`

Built for integration with Make.com, Zapier, or custom automations.
