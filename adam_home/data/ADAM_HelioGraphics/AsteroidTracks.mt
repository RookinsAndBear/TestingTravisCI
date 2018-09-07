stk.v.11.0
WrittenBy    STK_v11.3.0

BEGIN MTO

    Name		 AsteroidTracks
    BEGIN GeneralTrackData
        CentralBody		 Sun
        SaveTracks		 On
        SaveAsBinary		 Off
        IsStatic		 Off
        StaticGeometry		 Off
        BlockSize		 20
        StoredDataType		 21
        Epoch		 1 Jan 2018 00:00:00.000000
    END GeneralTrackData

    BEGIN DefaultTrack
        Id		 0
        InterpOrder		 0
        GreatArcInterp		 Off
    END DefaultTrack


    BEGIN Extensions

        BEGIN ADFFileData
        END ADFFileData

        BEGIN Desc
            BEGIN ShortText

            END ShortText
            BEGIN LongText

            END LongText
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics
            ShowAll		 Yes
            Show		 Yes

            BEGIN DefaultTrackGfx
                Show		 Yes
                MarkerColor		 #00ff00
                MarkerStyle		 0
                LabelColor		 #00ff00
                LineColor		 #00ff0000
                ShowMarker		 Yes
                ShowLabel		 No
                Font		 1
                ShowTrackLine		 Yes
                LineWidth		 1
                LineStyle		 0
                UseDisplayTime		 No
                DisplayTimes		 3600 3600
                TranslucentTrail		 No
                UsePreFadeTime		 No
                PreFadeTime		 0
                UsePostFadeTime		 No
                PostFadeTime		 0
            END DefaultTrackGfx
        END Graphics

        BEGIN VO
        END VO

    END Extensions
END MTO

