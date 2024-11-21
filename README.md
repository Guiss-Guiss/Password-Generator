# High Entropy Password Generator

A Python-based password generator leveraging time-seeded entropy for enhanced security.

## Security Features

- 🔒 Uses system time as entropy source (Unix timestamp)
- 🎲 Multiple layers of randomization:
  - Time-based seed
  - Character list shuffling
  - Individual character selection
  - Final password shuffling
- 🔡 Rich character set including:
  - Uppercase & lowercase letters
  - Numbers
  - Special characters

## Entropy Sources
```
Primary: Unix timestamp (seconds since epoch)
Secondary: Multiple shuffle operations
Character Space: 26 (lowercase) + 26 (uppercase) + 10 (digits) + 26 (special) = 88 characters
```

## Security Considerations

⚠️ **Important Notes:**
- Predictable if generation time is known
- Suitable for casual use
- Not recommended for cryptographic applications

## Recommendations

For higher security:
- Use `secrets` module instead of `random`
- Consider adding additional entropy sources

## Usage
```bash
python password.py
```

Follow prompts to:
1. Choose to generate password (y/n)
2. Specify desired length
3. Generate additional passwords as needed

## License
MIT License
