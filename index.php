<?php include 'header.php'; ?>
<section>
  <form action="index.php" method="post">
    <input name="url" type="text" autofocus placeholder="Reduced URL"/><input value="Run" type="submit" />
  </form>
  <?php
  if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['url'])) {
    $url = $_POST['url'];

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_HEADER, true);    // we want headers
    curl_setopt($ch, CURLOPT_NOBODY, true);    // we don't need body
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    $response = curl_exec($ch);

    if(! empty($response)) {
      $n_httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      $effective_url = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
      $redirect_url = curl_getinfo($ch, CURLINFO_REDIRECT_URL);
      curl_close($ch);
      if($n_httpcode >= 200 && $n_httpcode <400) {
        $urls = array($effective_url, $redirect_url);
        echo "<ul>";
        foreach ($urls as $u) {
          echo "<li>$u</li>";
        }
        echo "</ul>";
      }
      else {
        echo "<p class=\"error\">The request failed.</p>";
      }
    }
    else {
      echo "<p class=\"error\">Invalid URL.</p>";
    }
  }
  ?>
</section>
<?php include 'footer.php'; ?>
