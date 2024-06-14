<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Scraping Billboard and Creating Spotify Playlist</h1>
    <p>This Python script automates the process of scraping Billboard's Hot 100 songs for a specified date and creating a private playlist on Spotify with those songs. It utilizes web scraping with BeautifulSoup and interacts with the Spotify API using the Spotipy library.</p>

  <h2>Prerequisites</h2>
    <h3>Python Environment:</h3>
    <ul>
        <li>Python 3.x installed on your system.</li>
    </ul>
    <h3>Install Required Libraries:</h3>
    <pre><code>pip install beautifulsoup4 requests spotipy python-dotenv</code></pre>

  <h3>Spotify Developer Account:</h3>
    <ul>
        <li>Create a Spotify Developer account at <a href="https://developer.spotify.com/dashboard/applications" target="_blank">Spotify Developer Dashboard</a>.</li>
        <li>Create a new application to obtain Client ID and Client Secret.</li>
    </ul>

  <h2>Setup Instructions</h2>
    <h3>1. Obtain Spotify API Credentials</h3>
    <h4>Create a Spotify Application:</h4>
    <ul>
        <li>Log in to your Spotify Developer account and create a new application.</li>
        <li>Note down the Client ID and Client Secret provided for your application.</li>
    </ul>
    <h4>Set Redirect URI:</h4>
    <ul>
        <li>In your Spotify application settings, add <code>http://example.com</code> as a Redirect URI.</li>
    </ul>

  <h3>2. Prepare .env File</h3>
    <h4>Create .env File:</h4>
    <ul>
        <li>Create a file named <code>.env</code> in the same directory as your Python script.</li>
        <li>Add the following lines to the <code>.env</code> file, replacing placeholders with your actual credentials:</li>
    </ul>
    <pre><code>SPOTIFY_APP_CLIENT=your_client_id
SPOTIFY_APP_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URL=http://example.com</code></pre>

  <h3>3. Create token.txt File</h3>
    <ul>
        <li>Create an empty file named <code>token.txt</code> in the same directory as your Python script.</li>
    </ul>

  <h3>4. Run the Script</h3>
    <h4>Execute the Script:</h4>
    <ul>
        <li>Open a terminal or command prompt.</li>
        <li>Navigate to the directory containing your Python script and <code>.env</code> file.</li>
        <li>Run the script using Python:</li>
    </ul>
    <pre><code>python main.py</code></pre>

  <h4>Follow the Script Prompts:</h4>
    <ul>
        <li>Enter the date in the format <code>YYYY-MM-DD</code> when prompted. This date specifies the Billboard Hot 100 chart to scrape.</li>
        <li>Enter a custom name for the playlist you want to create on Spotify.</li>
    </ul>

  <h4>Authentication:</h4>
    <ul>
        <li>The script will open a web browser for you to log in to Spotify (if not already authenticated) and authorize the application.</li>
        <li>This step grants the script permission to create a playlist and add songs to your Spotify account.</li>
    </ul>

  <h2>How It Works</h2>
    <h3>Web Scraping Billboard:</h3>
    <ul>
        <li>The script uses <code>requests</code> and <code>BeautifulSoup</code> to scrape Billboard's Hot 100 songs page for the specified date.</li>
        <li>It extracts the song titles from the HTML response.</li>
    </ul>

  <h3>Spotify Authentication:</h3>
    <ul>
        <li>Authentication with Spotify is handled using <code>spotipy</code> and <code>SpotifyOAuth</code>.</li>
        <li>The script prompts for Spotify login and authorization via the web browser.</li>
        <li>It requests necessary permissions (<code>playlist-modify-private</code> and <code>playlist-read-private</code>) to manage playlists on your behalf.</li>
    </ul>

  <h3>Searching and Adding Songs:</h3>
    <ul>
        <li>For each song title scraped from Billboard, the script searches Spotify for a matching track from the same year.</li>
        <li>If found, the Spotify URI for the track is collected.</li>
    </ul>

  <h3>Playlist Creation and Population:</h3>
    <ul>
        <li>After collecting Spotify URIs for all matching tracks, the script prompts for a custom playlist name.</li>
        <li>It creates a new private playlist on your Spotify account with the specified name and adds the collected songs.</li>
    </ul>

  <h3>Completion:</h3>
    <ul>
        <li>Upon successful completion, the script confirms the playlist creation and exits.</li>
    </ul>
</body>
</html>
