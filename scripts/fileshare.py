#!/bin/bash

# Get the Dock Status
dockStatus=$(/usr/bin/pgrep -x 'Dock')

while [[ "$dockStatus" == "" ]]
do
    echo Dock not up, waiting...
    sleep 5
    dockStatus=$(/usr/bin/pgrep -x 'Dock')
done

exclude=("root" "ladmin")
user=`whoami`
echo $user

#Check to see if user is in the exclude list, if so exit
for x in "${exclude[@]}"; do
    if [ "$x" == "$user" ]; then
        logger "$user is a local user. Exiting..."
        exit 0
    fi
done

#====== Mount Mac Home =======

echo Mounting Mac Home
#open "smb://macsrv01.alleyns.local/MacHomes/MAC-$user"
/usr/bin/osascript -e "try" -e "mount volume \"smb://macsrv01.alleyns.local/MacHomes/MAC-$user\"" -e "end try"

#====== Sym Link local to network =======
mounted=1
folders=("Desktop" "Documents" "Movies" "Music" "Pictures")

echo "starting redirects"

#Check whether the MAC home is mounted and sleep if not
while [ $mounted -gt 0 ]; do
    echo "sleeping"
    sleep 1
    
     if [ -d /Volumes/MAC-$user ]; then

        for i in "${folders[@]}"; do
 
            if [ ! -d /Volumes/MAC-$user/$i ]; then
                mkdir -p /Volumes/MAC-$user/$i
            fi

            if [ ! -L /Users/$user/$i ]; then

                if [ ! -d /Users/$user/Local\ Data ]; then
                    mkdir /Users/$user/Local\ Data
                fi

                mv /Users/$user/$i /Users/$user/Local\ Data/$i
                ln -s /Volumes/MAC-$user/$i /Users/$user/
            fi

        done

        mounted=`expr $mounted - 1`
        
        #Refresh Finder
        killall Finder
    else
        echo "/Volumes/MAC-$user not available, waiting..."
    fi
done

#====== Set Sidebar =======

while [[ "$finderStatus" == "" ]]
do
	echo Finder not up, waiting...
    sleep 3
    finderStatus=$(/usr/bin/pgrep -x 'Finder')
done

/usr/local/bin/mysides remove all
/usr/local/bin/mysides add Mac\ Home file:///Volumes/MAC-$user
/usr/local/bin/mysides add Applications file:///Applications
/usr/local/bin/mysides add Desktop file:///Volumes/MAC-$user/Desktop
/usr/local/bin/mysides add Documents file:///Volumes/MAC-$user/Documents
/usr/local/bin/mysides add Downloads file:///Users/$user/Downloads
/usr/local/bin/mysides add Movies file:///Volumes/MAC-$user/Movies
/usr/local/bin/mysides add Music file:///Volumes/MAC-$user/Music
/usr/local/bin/mysides add Pictures file:///Volumes/MAC-$user/Pictures
/usr/local/bin/mysides add Local\ Data file:///Users/$user/Local%20Data

#====== Mount ART Shares =======

#Check if this is an Art Mac and then mount relevant shares
if [ "$(echo $HOSTNAME | grep -i -o "ART")" = "ART" ]; then

    /usr/bin/osascript -e "try" -e "mount volume \"smb://newtoy/art_scratch_space$\"" -e "end try" && /usr/local/bin/mysides add art_scratch_space file:///Volumes/art_scratch_space$ &

    group="Year 7 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 7"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 7\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 7 file:///Volumes/MAC-Art%20Year%207 &
    else
        echo "Not a member of $group"
    fi

    group="Year 8 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 8"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 8\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 8 file:///Volumes/MAC-Art%20Year%208 &
    else
        echo "Not a member of $group"
    fi

    group="Year 9 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 9"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 9\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 9 file:///Volumes/MAC-Art%20Year%209 &
    else
        echo "Not a member of $group"
    fi

    group="Year 10 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 10"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 10\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 10 file:///Volumes/MAC-Art%20Year%2010 &
    else
        echo "Not a member of $group"
    fi

    group="Year 11 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 11"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 11\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 11 file:///Volumes/MAC-Art%20Year%2011 &
    else
        echo "Not a member of $group"
    fi

    group="Year 12 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 12"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 12\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 12 file:///Volumes/MAC-Art%20Year%2012 &
    else
        echo "Not a member of $group"
    fi

    group="Year 13 Art"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Year 13"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Year 13\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Year\ 13 file:///Volumes/MAC-Art%20Year%2013 &
    else
        echo "Not a member of $group"
    fi

    group="Art Staff"
    if [[ $(dsmemberutil checkmembership -U "$user" -G "$group") =~ "is a member" ]]; then
        echo "Member of $group"
        #open "afp://macsrv01/MAC-Art Scratch Space"
        /usr/bin/osascript -e "try" -e "mount volume \"afp://macsrv01/MAC-Art Scratch Space\"" -e "end try" && /usr/local/bin/mysides add MAC-Art\ Scratch\ Space file:///Volumes/MAC-Art%20Scratch%20Space &
    else
        echo "Not a member of $group"
    fi
    
    #Mount shares from PC server (note: password contains a ! which is escaped with a \)
    #open smb://artepsonprintuser:Macprinting\!@artc23-wk01/artpcorange
    #open smb://artepsonprintuser:Macprinting\!@artc23-wk02/artpcblue
    /usr/bin/osascript -e "try" -e "mount volume \"smb://artepsonprintuser:Macprinting!@artc23-wk01/artpcorange\"" -e "end try" && /usr/local/bin/mysides add artpcorange file:///Volumes/artpcorange &
    /usr/bin/osascript -e "try" -e "mount volume \"smb://artepsonprintuser:Macprinting!@artc23-wk02/artpcblue\"" -e "end try" && /usr/local/bin/mysides add artpcblue file:///Volumes/artpcblue &
fi

#====== Mount MUSIC Shares =======

#Check if this is an Music Mac and then mount relevant shares
if [ "$(echo $HOSTNAME | grep -i -o "MUSIC")" = "MUSIC" ]; then
    /usr/bin/osascript -e "try" -e "mount volume \"smb://newtoy/pupil_share$/Music Class Resources\"" -e "end try" && /usr/local/bin/mysides add Music\ Class\ Resources file:///Volumes/Music%20Class%20Resources &
fi

#====== Mount STAFF Shares =======

#Mount Department shares for Teaching Staff
group1="Teachers"
group2="Junior School Teaching Staff"
group3="Junior School Support Staff"
group4="Senior School Teaching Staff"
group5="Senior School Support Staff"

if [[ $(dsmemberutil checkmembership -U "$user" -G "$group1") =~ "is a member" ]] || [[ $(dsmemberutil checkmembership -U "$user" -G "$group2") =~ "is a member" ]] || [[ $(dsmemberutil checkmembership -U "$user" -G "$group3") =~ "is a member" ]] || [[ $(dsmemberutil checkmembership -U "$user" -G "$group4") =~ "is a member" ]] || [[ $(dsmemberutil checkmembership -U "$user" -G "$group5") =~ "is a member" ]]; then
    echo "Mounting department share"
    #open "smb://minorityreport/departments$"
    /usr/bin/osascript -e "try" -e "mount volume \"smb://minorityreport/departments$\"" -e "end try" && /usr/local/bin/mysides add departments$ file:///Volumes/departments$ &
else
    echo "Do not mount department share"
fi

exit 0