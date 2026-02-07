# 🌹 Rose Day Surprise Website 🌹

A beautiful, interactive website to celebrate Rose Day with your girlfriend, even from a distance!

## ✨ Features

- **Animated Flower Bouquets**: Beautiful display of various flower bouquets with animations
- **Stickman Illustration**: A cute animated stickman (you!) giving flowers
- **Interactive Message Cards**: 6 special thought cards that flip to reveal personalized messages
- **Romantic Design**: Soft pink colors, floating petals, and smooth animations
- **Mobile Friendly**: Works perfectly on phones and computers

## 🚀 How to Use

### Method 1: Simple Python Server (Recommended)

1. **Make sure both files are in the same folder:**
   - `rose_day_surprise.html`
   - `start_server.py`

2. **Run the server:**
   ```bash
   python start_server.py
   ```
   
   Or if you have Python 3:
   ```bash
   python3 start_server.py
   ```

3. **Share the link:**
   - The script will display a link like: `http://192.168.x.x:8000/rose_day_surprise.html`
   - Copy this link and send it to your girlfriend via WhatsApp
   - She can open it on her phone or computer!

4. **Keep the server running:**
   - Don't close the terminal window while she's viewing the site
   - Press `Ctrl+C` to stop the server when done

### Method 2: Just Open the HTML File

If you just want to preview it yourself:
- Simply double-click `rose_day_surprise.html`
- It will open in your default web browser

## 📝 Customizing the Messages

You can personalize the thought card messages by editing the `rose_day_surprise.html` file:

1. Open `rose_day_surprise.html` in a text editor
2. Find the section with `const messages = [`
3. Edit the text between the quotes to add your own personal messages
4. Save the file and refresh the website

Example:
```javascript
{
    emoji: "🌹",
    text: "Your own personalized message here!"
}
```

## 💡 Tips for Sharing

### If she's on the same WiFi network:
- Just share the link the Python script gives you
- She can open it directly!

### If she's on a different network:
Consider these options:
1. **Use a service like ngrok** (for temporary public URL)
2. **Upload to a free hosting service** like Netlify, Vercel, or GitHub Pages
3. **Send her the HTML file directly** via WhatsApp and she can open it locally

### Easy Upload to Free Hosting:

**GitHub Pages (Free & Easy):**
1. Create a free GitHub account
2. Create a new repository
3. Upload `rose_day_surprise.html`
4. Enable GitHub Pages in settings
5. Share the generated URL!

**Netlify Drop (Easiest):**
1. Go to https://app.netlify.com/drop
2. Drag and drop the `rose_day_surprise.html` file
3. Get an instant shareable link!

## 🎨 What She'll See

1. **Beautiful Header** with "Happy Rose Day" greeting
2. **6 Animated Bouquet Cards** with different flower types
3. **Cute Stickman Animation** of you holding flowers
4. **6 Interactive Message Cards** she can flip through to read your thoughts
5. **Floating Rose Petals** in the background
6. **Romantic Footer** message

## ❤️ Making it Special

The messages included are sweet and romantic, but feel free to:
- Add your own inside jokes
- Reference special memories
- Include things specific to your relationship
- Change the number of cards (just add/remove message objects)

## 📱 Mobile Optimized

The website is fully responsive and looks great on:
- Phones (iPhone, Android)
- Tablets
- Desktop computers

## 🌟 Enjoy!

Happy Rose Day! May this virtual surprise bring a smile to her face and warmth to her heart! 🌹💕

---

*Made with love for Rose Day 2026* ❤️
