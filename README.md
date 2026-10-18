# Tubedoku Station Tracker 🚇

A zero-dependency, single-file web application hosted on GitHub Pages that tracks London Underground station frequencies from your [tubedoku.com](https://tubedoku.com) game history and surfaces unused stations across the network.

---

## Features (Phase 1)

- **Mobile Bookmarklet Generator**:
  - 1-tap copy button for a mobile bookmarklet script.
  - Interactive guides for **iOS Safari** and **Android Chrome**.
  - Extracts `archivedAnswers` and `completedPuzzles` from `tubedoku.com`'s `localStorage` and securely redirects to your tracker with a base64 encoded query parameter (`?data=...`).
- **Station Frequency Analyzer**:
  - Normalizes station names against all 272 London Underground stations.
  - Ranks stations from most-used to least-used.
  - Displays usage counts, percentage of total answers, relative frequency visualizer, and authentic TfL line badges.
  - Real-time search and filter by Tube line and Fare Zone.
- **Unused Station Discovery ("The Dream")**:
  - Cross-references your historical answers against the 272 official TfL stations.
  - Shows which stations you have never entered, filterable by Tube line and Fare Zone.
  - Live progress bar showing your network coverage percentage.
- **Persistence & Privacy**:
  - Automatically caches imported data in your tracker's `localStorage` so you don't need to re-run the bookmarklet on every visit.
  - Cleans the URL query parameter (`history.replaceState`) on load.
  - 100% client-side: your game data never leaves your device.
  - Includes manual JSON backup, download, and paste drawer.

---

## How to Set Up Mobile Export (iOS & Android)

### iOS (Safari)
1. Open your tracker page on your iPhone.
2. Tap the **Share icon** &rarr; tap **Add Bookmark** &rarr; name it `Export Tubedoku` &rarr; tap **Save**.
3. In the tracker app, go to **Bookmarklet Setup** and tap **Copy Bookmarklet Code**.
4. Tap the **Bookmarks icon** (open book) &rarr; tap **Edit** (bottom right) &rarr; tap `Export Tubedoku` &rarr; replace the URL with the copied script &rarr; tap **Done**.
5. Go to [tubedoku.com](https://tubedoku.com) where you play.
6. Tap the Safari address bar, type `Export Tubedoku`, and tap the matching bookmark. It will extract your answers and redirect back to your tracker!

### Android (Chrome)
1. Open your tracker page in Chrome.
2. Tap the **3-dots menu (&vellip;)** &rarr; tap the **Star icon (&star;)** to bookmark.
3. In the tracker app, go to **Bookmarklet Setup** and tap **Copy Bookmarklet Code**.
4. Open the 3-dots menu &rarr; **Bookmarks** &rarr; tap the 3 dots next to the bookmark &rarr; **Edit**.
5. Set Name to `Export Tubedoku` and paste the script into the **URL field** &rarr; Save.
6. Open [tubedoku.com](https://tubedoku.com). In Chrome's address bar, type `Export Tubedoku` and tap the bookmark suggestion to run it.

---

## GitHub Pages Deployment

1. Commit and push `index.html` to the `main` branch of this repository (`mikeyt23/tubedoku-map`).
2. Go to **Settings** &rarr; **Pages** in GitHub.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`, choose `main` branch and `/ (root)`.
4. Your tracker will be live at:
   ```
   https://mikeyt23.github.io/tubedoku-map/
   ```

---

## Phase 2 Roadmap

- **Interactive TfL Schematic Map**: Visualise all 272 stations on the classic London Underground map.
- **Heatmap Overlay**: Color-coded stations reflecting usage intensity, with unplayed stations dimmed or highlighted.
