/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "./**/*.js"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        surface: 'var(--surface)',
        'surface-container-lowest': 'var(--surface-container-lowest)',
        'surface-container-low': 'var(--surface-container-low)',
        'surface-container': 'var(--surface-container)',
        'surface-container-high': 'var(--surface-container-high)',
        'on-surface': 'var(--on-surface)',
        'on-surface-variant': 'var(--on-surface-variant)',
        outline: 'var(--outline)',
        'outline-variant': 'var(--outline-variant)',
        primary: 'var(--primary)',
        'on-primary': 'var(--on-primary)',
        secondary: 'var(--secondary)',
        'secondary-container': 'var(--secondary-container)',
        'on-secondary-container': 'var(--on-secondary-container)',
        background: 'var(--background)',
        'on-background': 'var(--on-background)',
      },
      fontFamily: { inter: ['Inter', 'sans-serif'], space: ['Space Grotesk', 'sans-serif'], serif: ['Georgia', 'serif'] },
      borderRadius: { sm: '0.25rem', DEFAULT: '0.5rem', md: '0.75rem', lg: '1rem', xl: '1.5rem', full: '9999px' },
      fontSize: {
        'headline-lg': ['3.5rem', { lineHeight: '1.1', letterSpacing: '-0.04em', fontWeight: '700' }],
        'headline-md': ['2rem', { lineHeight: '1.2', letterSpacing: '-0.02em', fontWeight: '600' }],
        'body-lg': ['1.125rem', { lineHeight: '1.6', letterSpacing: '-0.01em', fontWeight: '400' }],
        'body-sm': ['0.875rem', { lineHeight: '1.5', letterSpacing: '0', fontWeight: '400' }],
      },
    }
  }
}
