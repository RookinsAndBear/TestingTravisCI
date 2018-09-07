stk.v.11.0
WrittenBy    STK_v11.3.0

BEGIN Planet

    Name		 Mercury

    BEGIN PathDescription

        CentralBody		 Mercury
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 0

            JplSpiceId		 199

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		 2.4515450000000000e+06
            OrbitMeanDist		 5.7909175407278999e+10
            OrbitEcc		 2.0563069000000000e-01
            OrbitInc		 2.8552056770743999e+01
            OrbitRAAN		 1.0987976077726001e+01
            OrbitPerLong		 7.8552531375219999e+01
            OrbitMeanLong		 2.5334692137521998e+02
            OrbitMeanDistDot		 2.7032058644763999e+00
            OrbitEccDot		 6.9185489390828003e-10
            OrbitIncDot		 1.1729337539006999e-07
            OrbitRAANDot		 -9.1090591464276004e-07
            OrbitPerLongDot		 4.2766341566708997e-06
            OrbitMeanLongDot		 4.0923387105835003e+00

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		 2.2032090000000000e+13
        Radius		 2.4397000000000000e+06
        Magnitude		 0.0000000000000000e+00
        ReferenceDistance		 0.0000000000000000e+00

    END PhysicalData

    BEGIN AutoRename

        AutoRename		 Yes

    END AutoRename

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals
        END AccessConstraints

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #d292e2
                LabelColor		 #d292e2
                LineColor		 #d292e2
                LineStyle		 0
                LineWidth		 2
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 Off
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 Off
                ShowSubPlanetLabel		 Off
                ShowOrbit		 On
                NumOrbitPoints		 360
                OrbitTime		 7.6005607031260002e+06
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

