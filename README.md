# Google Trends Crawler

This code retrieves the trend curve of Google Trend for any given query term. Basically this program works with Google Trend APIs (as obtained from Google Trends Network traffic) to download trend curves in a manageable format (JSON).

This code just proxies a Google query to obtain a JSON file as result from Google Servers.

## Usage

 *python getTrends.py QUERY [FILE] [LOCALE]*

 * **QUERY**: The query to perform, for using spaces just surround everything with quotes
 * **FILE**: (OPTIONAL) The filename where the information will be stored in JSON format. If no file is provided the resulting query is displayed in JSON in the command line.
 * **LOCALE**: The locale of the query; defaults to "en-US"

 ## Requirements

 * **Python requirements**: requests module

 ## Issues

 There are problems with the queries due to time differences. Timezone is not dynamic and thus the program may fail when the day of the month is different.