# knock_knock

knock_knock is a project that is pretending to be a victim that is connecting to C2s, and configuration hosts.
The idea is to communicate to various configurations hosts such as Mastodon and Telegram and receiving "fresh" C2 addresses.

# Operating
In order to use this tool, you need to add to the mastodon_profiles.txt file Mastodon profile's handler in each line.
For example, if we have a profile url: https://mas.to/@example, we will add "example" to the mastodon_profiles.txt file.

# Output
The output of the file is being added to the malicious_urls.json file, each address that will be gathered from the Mastodon profile will be added to this json file as a key and will add the user as value like so:

  {
    "http://11.22.33.44:8080":
      ['user1', 'user2', 'user3']
  }
 
 
