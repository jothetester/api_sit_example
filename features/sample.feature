Feature:A spotify user can create and amend playlists
  Scenario: Creating and adding one song to a playlist
    Given that a playlist called blah songs is created in my spotify account
    When  I search for a track from album called star wars
    And   I add my favourite track to my playlist
    Then  my favourite track is available in my playlist

