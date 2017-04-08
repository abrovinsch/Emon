L="sv"
TWEETSFILE="$L/_emojitweets.txt"

cd /Users/oskar/Egna\ Dokument/Programmering/Emon

echo "Cleaning the file $TWEETSFILE…"
echo ""
echo ""
python3 cleanfile.py $TWEETSFILE

echo ""
echo ""
echo "Making emoji table…"
echo ""
echo ""
python3 makeemojitable.py $TWEETSFILE "$L/emojifrequencies.csv"

echo ""
echo ""
echo "Removing the old found words file…"
cd /Users/oskar/Egna\ Dokument/Programmering/Emon/$L
mv "foundwords.csv" "old_foundwords.csv"
echo ""
echo "Done!"